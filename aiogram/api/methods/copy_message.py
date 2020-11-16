from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from ..types import (
    UNSET,
    ForceReply,
    InlineKeyboardMarkup,
    MessageEntity,
    MessageId,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from .base import Request, TelegramMethod, prepare_parse_mode

if TYPE_CHECKING:  # pragma: no cover
    from ..client.bot import Bot


class CopyMessage(TelegramMethod[MessageId]):
    """
    Use this method to copy messages of any kind. The method is analogous to the method
    forwardMessages, but the copied message doesn't have a link to the original message. Returns
    the MessageId of the sent message on success.

    Source: https://core.telegram.org/bots/api#copymessage
    """

    __returning__ = MessageId

    chat_id: Union[int, str]
    """Unique identifier for the target chat or username of the target channel (in the format
    @channelusername)"""
    from_chat_id: Union[int, str]
    """Unique identifier for the chat where the original message was sent (or channel username in
    the format @channelusername)"""
    message_id: int
    """Message identifier in the chat specified in from_chat_id"""
    caption: Optional[str] = None
    """New caption for media, 0-1024 characters after entities parsing. If not specified, the
    original caption is kept"""
    parse_mode: Optional[str] = UNSET
    """Mode for parsing entities in the new caption. See formatting options for more details."""
    caption_entities: Optional[List[MessageEntity]] = None
    """List of special entities that appear in the new caption, which can be specified instead of
    parse_mode"""
    disable_notification: Optional[bool] = None
    """Sends the message silently. Users will receive a notification with no sound."""
    reply_to_message_id: Optional[int] = None
    """If the message is a reply, ID of the original message"""
    allow_sending_without_reply: Optional[bool] = None
    """Pass True, if the message should be sent even if the specified replied-to message is not
    found"""
    reply_markup: Optional[
        Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
    ] = None
    """Additional interface options. A JSON-serialized object for an inline keyboard, custom reply
    keyboard, instructions to remove reply keyboard or to force a reply from the user."""

    def build_request(self, bot: Bot) -> Request:
        data: Dict[str, Any] = self.dict()

        prepare_parse_mode(
            bot, data, parse_mode_property="parse_mode", entities_property="caption_entities"
        )

        return Request(method="copyMessage", data=data)
