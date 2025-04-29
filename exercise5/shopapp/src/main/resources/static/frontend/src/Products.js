import React, { useEffect, useState } from 'react';

export default function Products({ onSelect }) {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        fetch('http://localhost:8080/api/products')
            .then(res => res.json())
            .then(setProducts)
            .catch(console.error);
    }, []);

    return (
        <div>
            <h2>Produkty</h2>
            <ul>
                {products.map(product => (
                    <li key={product.id}>
                        {product.name} - {product.price} zł
                        <button onClick={() => onSelect(product)}>Kup</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}
