package controllers

import (
	"exercise4/models"
	"net/http"
	"strconv"

	"github.com/labstack/echo/v4"
	"gorm.io/gorm"
)

type ProductController struct {
	DB *gorm.DB
}

func InitProductController(e *echo.Echo, db *gorm.DB) {
	controller := &ProductController{DB: db}

	e.GET("/products", controller.GetProducts)
}

func (p *ProductController) GetProducts(ctx echo.Context) error {
	categoryID, err := strconv.Atoi(ctx.QueryParam("categoryID"))
	if err != nil && ctx.QueryParam("categoryID") != "" {
		return ctx.JSON(http.StatusBadRequest, "Invalid category ID")
	}

	priceAbove, err := strconv.ParseFloat(ctx.QueryParam("priceAbove"), 64)
	if err != nil && ctx.QueryParam("priceAbove") != "" {
		return ctx.JSON(http.StatusBadRequest, "Invalid price")
	}

	query := p.DB.Model(&models.Product{})

	if categoryID > 0 {
		query = query.Scopes(models.BelongsToCategory(uint(categoryID)))
	}

	if priceAbove > 0 {
		query = query.Scopes(models.PriceAbove(priceAbove))
	}

	var products []models.Product
	if err := query.Find(&products).Error; err != nil {
		return ctx.JSON(http.StatusInternalServerError, "Could not retrieve products")
	}

	return ctx.JSON(http.StatusOK, products)
}
