package controllers

import play.api.mvc._

import javax.inject._

@Singleton
class ProductController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {
  val products = List("iPhone 15", "MacBook Pro", "iPad Air")

  def listProducts = Action {
    Ok(products.mkString(", "))
  }

  def getProduct(id: Int) = Action {
    if (id >= 0 && id < products.length) {
      Ok(s"Produkt o ID: $id: ${products(id)}")
    } else {
      NotFound(s"Produkt o ID: $id nie istnieje.")
    }
  }
}
