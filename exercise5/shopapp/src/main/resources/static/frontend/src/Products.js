import React, { useEffect, useState } from "react";

const Products = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        fetch("/api/products")
            .then((res) => res.json())
            .then((data) => setProducts(data));
    }, []);

    const handleBuy = (product) => {
        fetch("/api/payments", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ id: 0, product: product.name, amount: product.price }),
        });
    };

    return (
        <div>
            <h2>Produkty</h2>
            <ul>
                {products.map((product) => (
                    <li key={product.id}>
                        {product.name} – {product.price} zł{" "}
                        <button onClick={() => handleBuy(product)}>Kup</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Products;
