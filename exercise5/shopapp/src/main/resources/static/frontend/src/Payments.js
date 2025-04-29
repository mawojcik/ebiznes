import React, { useState } from 'react';

export default function Payments({ selectedProduct }) {
    const [quantity, setQuantity] = useState(1);
    const [message, setMessage] = useState('');

    const handlePay = () => {
        fetch('http://localhost:8080/api/payments', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                productId: selectedProduct.id,
                quantity: quantity
            })
        })
            .then(res => res.text())
            .then(setMessage)
            .catch(console.error);
    };

    if (!selectedProduct) return null;

    return (
        <div>
            <h2>Płatności</h2>
            <p>Produkt: {selectedProduct.name}</p>
            <input
                type="number"
                value={quantity}
                min="1"
                onChange={e => setQuantity(Number(e.target.value))}
            />
            <button onClick={handlePay}>Zapłać</button>
            <p>{message}</p>
        </div>
    );
}
