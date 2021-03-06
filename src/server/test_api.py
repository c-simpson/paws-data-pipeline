import pytest, socket, requests, os

#
# Run 'pytest' from the command line
#
# Running pytest can result in six different exit codes:
#   0 - All tests were collected and passed successfully
#   1 - Tests were collected and run but some of the tests failed
#   2 - Test execution was interrupted by the user
#   3 - Internal error happened while executing tests
#   4 - pytest command line usage error
#   5 - No tests were collected
#
# These codes are represented by the pytest.ExitCode enum


if os.getenv("IS_LOCAL") == "True":
    SERVER_URL = "http://localhost:3333"
    IS_LOCAL = True
else:
    SERVER_URL = "http://server:5000"
    IS_LOCAL = False

###  DNS lookup tests

# Ensure DNS not resolving bad host names
def test_bad_dns():
    with pytest.raises(socket.gaierror):
        socket.getaddrinfo("bad_server_name_that_should_not_resolve", "5000")


# Do we get IPs for good names?


@pytest.mark.skipif(IS_LOCAL, reason="Not run when IS_LOCAL")
def test_db_dns():
    assert (
        len(socket.getaddrinfo("db", "5000")) > 0
    )  # getaddrinfo works for IPv4 and v6


@pytest.mark.skipif(IS_LOCAL, reason="Not run when IS_LOCAL")
def test_server_dns():
    assert len(socket.getaddrinfo("server", "5000")) > 0


@pytest.mark.skipif(IS_LOCAL, reason="Not run when IS_LOCAL")
def test_client_dns():
    assert len(socket.getaddrinfo("client", "5000")) > 0


# Simple API tests


def test_currentFiles():
    response = requests.get(SERVER_URL + "/api/listCurrentFiles")
    assert response.status_code == 200


def test_statistics():
    response = requests.get(SERVER_URL + "/api/statistics")
    assert response.status_code == 200

