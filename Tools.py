class TranscribeTools(object):

    def __init__(self, toolName, toolRelativePath, lastModified):
        self._toolName = toolName;
        self._toolRelativePath = toolRelativePath;
        self._lastModified = lastModified;

    @property
    def fullName(self):
        return '{0} {1} {2]'.format(self._toolName, self._toolRelativePath, self._lastModified)
