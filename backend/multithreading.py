from PySide6.QtCore import QRunnable, QObject, Signal, QThreadPool


class SimpleWorker(QRunnable):
    class WorkerSignals(QObject):
        finished = Signal()
        error = Signal(Exception)
        result = Signal(object)

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

        self.__signals = self.WorkerSignals()
        self.finished = self.__signals.finished
        self.error = self.__signals.error
        self.result = self.__signals.result

    def run(self):
        try:
            result = self.func(*self.args, **self.kwargs)
        except Exception as e:
            self.error.emit(e)
        else:
            self.result.emit(result)
        finally:
            self.finished.emit()


def default_error_handler(err):
    raise err


def run_task(func, *args, result_slot=None, finished_slot=None, error_slot=default_error_handler, **kwargs):
    worker = SimpleWorker(func, *args, **kwargs)
    if result_slot is not None:
        worker.result.connect(result_slot)
    if finished_slot is not None:
        worker.finished.connect(finished_slot)
    worker.error.connect(error_slot)
    QThreadPool.globalInstance().start(worker)


def multithreaded(func):
    def wrapper(*args, result_slot=None, finished_slot=None, error_slot=default_error_handler, **kwargs):
        run_task(
            func, *args,
            result_slot=result_slot,
            finished_slot=finished_slot,
            error_slot=error_slot,
            **kwargs
        )
    return wrapper
