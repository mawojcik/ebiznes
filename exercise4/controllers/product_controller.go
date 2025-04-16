package controllers

import (
	"exercise4/models"
	"net/http"
	"github.com/labstack/echo/v4"
	"gorm.io/gorm"
)

type ProductController struct {
	DB *gorm.DB
}

func InitProductController(e *echo.Echo, db *gorm.DB) {
	controller := &ProductController{DB: db}

	e.POST("/products", controller.CreateProduct)
	e.GET("/products", controller.GetAllProducts)
	e.GET("/products/:id", controller.GetProduct)
	e.PUT("/products/:id", controller.UpdateProduct)
	e.DELETE("/products/:id", controller.DeleteProduct)
}

func (p *ProductController) CreateProduct(c echo.Context) error {
	product := new(models.Product)
	if err := c.Bind(product); err != nil {
		return c.JSON(http.StatusBadRequest, err.Error())
	}
	if err := p.DB.Create(product).Error; err != nil {
		return c.JSON(http.StatusInternalServerError, err.Error())
	}
	return c.JSON(http.StatusCreated, product)
}

func (p *ProductController) GetAllProducts(c echo.Context) error {
	var products []models.Product
	if err := p.DB.Find(&products).Error; err != nil {
		return c.JSON(http.StatusInternalServerError, err.Error())
	}
	return c.JSON(http.StatusOK, products)
}

func (p *ProductController) GetProduct(c echo.Context) error {
	id := c.Param("id")
	var product models.Product
	if err := p.DB.First(&product, id).Error; err != nil {
		return c.JSON(http.StatusNotFound, "Product not found")
	}
	return c.JSON(http.StatusOK, product)
}

func (p *ProductController) UpdateProduct(c echo.Context) error {
	id := c.Param("id")
	var product models.Product
	if err := p.DB.First(&product, id).Error; err != nil {
		return c.JSON(http.StatusNotFound, "Product not found")
	}

	if err := c.Bind(&product); err != nil {
		return c.JSON(http.StatusBadRequest, err.Error())
	}

	if err := p.DB.Save(&product).Error; err != nil {
		return c.JSON(http.StatusInternalServerError, err.Error())
	}
	return c.JSON(http.StatusOK, product)
}

func (p *ProductController) DeleteProduct(c echo.Context) error {
	id := c.Param("id")
	if err := p.DB.Delete(&models.Product{}, id).Error; err != nil {
		return c.JSON(http.StatusInternalServerError, err.Error())
	}
	return c.NoContent(http.StatusNoContent)
}
