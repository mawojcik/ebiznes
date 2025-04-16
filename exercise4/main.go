package main

import (
	"exercise4/controllers"
	"exercise4/models"

	"github.com/labstack/echo/v4"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

func main() {
	e := echo.New()

	db, err := gorm.Open(sqlite.Open("app.db"), &gorm.Config{})
	if err != nil {
		panic("could not connect to the database")
	}

	models.Migrate(db)
	controllers.InitProductController(e, db)
	controllers.InitCategoryController(e, db)
	controllers.InitCartController(e, db)

	e.Logger.Fatal(e.Start(":8080"))
}
