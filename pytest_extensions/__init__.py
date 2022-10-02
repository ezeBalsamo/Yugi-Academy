from _pytest._code import ExceptionInfo


def message_text(exception_info):
    tag = exception_info.value.args[0]
    return tag


ExceptionInfo.message_text = message_text
