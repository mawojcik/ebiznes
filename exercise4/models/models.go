package models

import (
	"gorm.io/gorm"
)

type User struct {
	gorm.Model
	Name  string
	Email string
}

type Order struct {
	gorm.Model
	UserID uint
	User   User
	Total  float64
}

type Review struct {
	gorm.Model
	ProductID uint
	Product   Product
	Content   string
	Rating    int
}
