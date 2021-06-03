cls = lambda: print("\033[2J\033[;H", end='')
cls()
"""
Day 56 - main
"""
import server

flask_server = server.Server()
app = flask_server.app

flask_server.run()
