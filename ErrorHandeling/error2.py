class myError(TypeError):
    """
    Exception raised when a specific error code is needed
    """

    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code


raise myError("This is my custom error.", 500)
