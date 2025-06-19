from behave import fixture, use_fixture
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions
from http.server import SimpleHTTPRequestHandler
from functools import partial
import socketserver
import threading
import pathlib

address = "127.0.0.1"
port = 8000


@fixture
def browser_firefox(context):
    options = FirefoxOptions()
    options.add_argument("-headless")
    context.browser = Firefox(options=options)
    yield context.browser
    context.browser.quit()


@fixture
def local_webserver(context):
    web_root = pathlib.Path(__file__).parent.parent.parent.joinpath("dist")

    handler_class = partial(SimpleHTTPRequestHandler, directory=web_root)

    socketserver.TCPServer.allow_reuse_address = True

    httpd = socketserver.TCPServer((address, port), handler_class)

    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    def shutdown_webserver():
        httpd.shutdown()
        httpd.server_close()
        server_thread.join()

    context.add_cleanup(shutdown_webserver)


def before_all(context):
    context.config.setup_logging()
    use_fixture(local_webserver, context)
    use_fixture(browser_firefox, context)
    context.address = address
    context.port = port
