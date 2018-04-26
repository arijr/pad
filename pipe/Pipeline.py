class Pipeline:

  def __init__(self,
                functions=(),
                input=(),
                terminals=(print,)):
    if hasattr(functions,'__call__'):
        self.functions = [functions]
    else:
        self.functions = list(functions)
    self.input = input
    self.terminals = [Ω] + list(terminals)

    Ω = lambda x: x
