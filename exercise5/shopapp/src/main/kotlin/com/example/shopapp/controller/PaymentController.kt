package com.example.shopapp.controller

import com.example.shopapp.model.Product
import com.example.shopapp.model.Payment
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/payments")
class PaymentController {
    @PostMapping
    fun processPayment(@RequestBody payment: Payment): String {
        println("Received payment: $payment")
        return "Payment processed"
    }
}