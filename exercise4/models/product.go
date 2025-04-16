package models

import "gorm.io/gorm"

type Product struct {
	gorm.Model
	Name        string  `json:"name"`
	Description string  `json:"description"`
	Price       float64 `json:"price"`
	CategoryID  uint    `json:"categoryID"`
	Category    Category `json:"category" gorm:"foreignKey:CategoryID"`
}

func PriceAbove(price float64) func(db *gorm.DB) *gorm.DB {
	return func(db *gorm.DB) *gorm.DB {
		return db.Where("price > ?", price)
	}
}

func BelongsToCategory(categoryID uint) func(db *gorm.DB) *gorm.DB {
	return func(db *gorm.DB) *gorm.DB {
		return db.Where("category_id = ?", categoryID)
	}
}
