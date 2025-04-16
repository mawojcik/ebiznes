package controllers

import (
	"exercise4/models"
	"net/http"
	"strconv"

	"github.com/labstack/echo/v4"
	"gorm.io/gorm"
)

type CartController struct {
	DB *gorm.DB
}

func InitCartController(e *echo.Echo, db *gorm.DB) {
	controller := &CartController{DB: db}

	e.POST("/carts/:userID/products/:productID", controller.AddToCart)
	e.GET("/carts/:userID", controller.GetCart)
}

func (c *CartController) AddToCart(ctx echo.Context) error {
	userID, err := strconv.Atoi(ctx.Param("userID"))
	if err != nil {
		return ctx.JSON(http.StatusBadRequest, "Invalid user ID")
	}

	productID, err := strconv.Atoi(ctx.Param("productID"))
	if err != nil {
		return ctx.JSON(http.StatusBadRequest, "Invalid product ID")
	}

	var cart models.Cart
	if err := c.DB.Where("user_id = ?", userID).First(&cart).Error; err != nil {
		cart = models.Cart{UserID: uint(userID)}
		if err := c.DB.Create(&cart).Error; err != nil {
			return ctx.JSON(http.StatusInternalServerError, "Could not create cart")
		}
	}

	var product models.Product
	if err := c.DB.First(&product, productID).Error; err != nil {
		return ctx.JSON(http.StatusNotFound, "Product not found")
	}
	
	if err := c.DB.Model(&cart).Association("Products").Append(&product); err != nil {
		return ctx.JSON(http.StatusInternalServerError, "Could not add product to cart")
	}

	return ctx.JSON(http.StatusOK, cart)
}

func (c *CartController) GetCart(ctx echo.Context) error {
	userID, err := strconv.Atoi(ctx.Param("userID"))
	if err != nil {
		return ctx.JSON(http.StatusBadRequest, "Invalid user ID")
	}

	var cart models.Cart
	if err := c.DB.Preload("Products").Where("user_id = ?", userID).First(&cart).Error; err != nil {
		return ctx.JSON(http.StatusNotFound, "Cart not found")
	}

	return ctx.JSON(http.StatusOK, cart)
}
