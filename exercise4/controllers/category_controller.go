package controllers

import (
	"exercise4/models"
	"net/http"
	"github.com/labstack/echo/v4"
	"gorm.io/gorm"
)

type CategoryController struct {
	DB *gorm.DB
}

func InitCategoryController(e *echo.Echo, db *gorm.DB) {
	controller := &CategoryController{DB: db}

	e.POST("/categories", controller.CreateCategory)
	e.GET("/categories", controller.GetAllCategories)
}

func (c *CategoryController) CreateCategory(ctx echo.Context) error {
	category := new(models.Category)
	if err := ctx.Bind(category); err != nil {
		return ctx.JSON(http.StatusBadRequest, err.Error())
	}
	if err := c.DB.Create(category).Error; err != nil {
		return ctx.JSON(http.StatusInternalServerError, err.Error())
	}
	return ctx.JSON(http.StatusCreated, category)
}

func (c *CategoryController) GetAllCategories(ctx echo.Context) error {
	var categories []models.Category
	if err := c.DB.Preload("Products").Find(&categories).Error; err != nil {
		return ctx.JSON(http.StatusInternalServerError, err.Error())
	}
	return ctx.JSON(http.StatusOK, categories)
}
