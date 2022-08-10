from typing import Any

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware


class CallbackAnswerMiddleware(BaseMiddleware):
    @staticmethod
    async def on_pre_process_callback_query(call: types.CallbackQuery, data: dict[Any, Any]) -> None:
        await call.answer()
