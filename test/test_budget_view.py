from code import budget_view
import mock
from mock import ANY
from mock.mock import patch
from telebot import types


@patch("telebot.telebot")
def test_display_overall_budget(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True
    mocker.patch.object(budget_view, "helper")
    budget_view.helper.getOverallBudget.return_value = ""
    message = create_message("hello from testing")
    budget_view.display_overall_budget(message, mc)
    assert mc.send_message.called


@patch("telebot.telebot")
def test_display_category_budget(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True
    mocker.patch.object(budget_view, "helper")
    dummy_categ_val = {
        "Food": 10.0,
        "Transport": 50.0,
        "Shopping": 148.0,
        "Miscellaneous": 47.93,
        "Miscellaneous": 47.93,
        "Utilities": 200.0,
        "Groceries": 55.21,
    }
    budget_view.helper.getCategoryBudget.return_value = dummy_categ_val
    message = create_message("hello from testing")
    budget_view.display_category_budget(message, mc)
    assert mc.send_photo.called


@patch("telebot.telebot")
def test_run_overall_budget(mock_telebot, mocker):
    mc = mock_telebot.return_value

    mocker.patch.object(budget_view, "helper")
    budget_view.helper.isOverallBudgetAvailable.return_value = True

    budget_view.display_overall_budget = mock.Mock(return_value=True)
    message = create_message("hello from testing")
    budget_view.run(mc, message)

    assert budget_view.display_overall_budget.called


@patch("telebot.telebot")
def test_run_category_budget(mock_telebot, mocker):
    mc = mock_telebot.return_value

    mocker.patch.object(budget_view, "helper")
    budget_view.helper.isCategoryBudgetAvailable.return_value = True
    budget_view.helper.isOverallBudgetAvailable.return_value = False

    budget_view.display_category_budget = mock.Mock(return_value=True)

    message = create_message("hello from testing")
    budget_view.run(mc, message)
    assert budget_view.display_category_budget.called


@patch("telebot.telebot")
def test_run_failing_case(mock_telebot, mocker):
    mc = mock_telebot.return_value

    mocker.patch.object(budget_view, "helper")
    budget_view.helper.isCategoryBudgetAvailable.return_value = False
    budget_view.helper.isOverallBudgetAvailable.return_value = False
    budget_view.helper.throw_exception.return_value = True

    message = create_message("hello from testing")
    budget_view.run(mc, message)
    assert budget_view.helper.throw_exception.called


def create_message(text):
    params = {"messagebody": text}
    chat = types.User(11, False, "test")
    message = types.Message(1, None, None, chat, "text", params, "")
    message.text = text
    return message
