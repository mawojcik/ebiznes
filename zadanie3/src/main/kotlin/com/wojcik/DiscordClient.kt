package com.wojcik

import dev.kord.common.entity.Snowflake
import dev.kord.rest.service.RestClient

class DiscordClient(private val token: String) {
    private val rest = RestClient(token)

    suspend fun sendMessage(channelId: String, message: String) {
        rest.channel.createMessage(Snowflake(channelId)) {
            content = message
        }
    }
}