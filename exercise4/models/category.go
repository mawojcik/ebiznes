package models

import "gorm.io/gorm"

type Category struct {
	gorm.Model
	Name     string    `json:"name"`
	Products []Product `json:"products,omitempty"`
}

func ByName(name string) func(db *gorm.DB) *gorm.DB {
	return func(db *gorm.DB) *gorm.DB {
		return db.Where("name = ?", name)
	}
}
