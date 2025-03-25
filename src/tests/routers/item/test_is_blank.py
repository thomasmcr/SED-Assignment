from fastapi.testclient import TestClient
from sqlmodel import Session
from src.routers.item_router import isBlank

# Test for empty string
def test_is_blank_empty_string(client: TestClient, session: Session):
    assert isBlank("") is True

# Test for non-empty string
def test_is_blank_non_empty_string(client: TestClient, session: Session):
    assert isBlank("Test") is False

# Test for string with whitespace only
def test_is_blank_whitespace_only(client: TestClient, session: Session):
    assert isBlank("   ") is True

# Test for string with mixed whitespace and characters
def test_is_blank_mixed_whitespace_characters(client: TestClient, session: Session):
    assert isBlank("  Test  ") is False

# Test for string with special characters
def test_is_blank_special_characters(client: TestClient, session: Session):
    assert isBlank("@#%") is False

# Test for string with numbers only
def test_is_blank_numbers_only(client: TestClient, session: Session):
    assert isBlank("123") is False

# Test for string with a combination of whitespace and special characters
def test_is_blank_whitespace_and_special_characters(client: TestClient, session: Session):
    assert isBlank("   @#%   ") is False

# Test for string with a combination of whitespace and numbers
def test_is_blank_whitespace_and_numbers(client: TestClient, session: Session):
    assert isBlank("   123   ") is False

# Test for None (null) input
def test_is_blank_none_input(client: TestClient, session: Session):
    assert isBlank(None) is True

# Test for a very long empty string
def test_is_blank_long_empty_string(client: TestClient, session: Session):
    assert isBlank(" " * 1000) is True