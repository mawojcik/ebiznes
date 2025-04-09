package com.wojcik

import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.server.request.*
import io.ktor.server.response.*
import io.ktor.server.routing.*

fun main() {
    val channelId = "--------"
    val discordClient = DiscordClient("--------")


    embeddedServer(Netty, port = 8080) {
        messageSenderModule(discordClient, channelId)
    }.start(wait = true)
}

fun Application.messageSenderModule(discordClient: DiscordClient, channelId: String) {
    routing {
        post("/send") {
            val message = call.receive<String>()
            discordClient.sendMessage(channelId, message)
            call.respond("Message was sent to channel with id $channelId.\n")
        }
    }
}

