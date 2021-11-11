from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        _toml = toml.loads(content)

        return Project(_toml["tool"]["poetry"]["name"], _toml["tool"]["poetry"]["description"], _toml["tool"]["poetry"]["dependencies"].keys(), _toml["tool"]["poetry"]["dev-dependencies"].keys())
