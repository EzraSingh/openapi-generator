/*
 * OpenAPI Petstore
 *
 * This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.
 *
 * API version: 1.0.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package petstoreserver

import (
	"github.com/gin-gonic/gin"
)

type StoreAPI struct {
}

// Delete /v2/store/order/:orderId
// Delete purchase order by ID 
func (api *StoreAPI) DeleteOrder(c *gin.Context) {
	// Your handler implementation
	c.JSON(200, gin.H{"status": "OK"})
}

// Get /v2/store/inventory
// Returns pet inventories by status 
func (api *StoreAPI) GetInventory(c *gin.Context) {
	// Your handler implementation
	c.JSON(200, gin.H{"status": "OK"})
}

// Get /v2/store/order/:orderId
// Find purchase order by ID 
func (api *StoreAPI) GetOrderById(c *gin.Context) {
	// Your handler implementation
	c.JSON(200, gin.H{"status": "OK"})
}

// Post /v2/store/order
// Place an order for a pet 
func (api *StoreAPI) PlaceOrder(c *gin.Context) {
	// Your handler implementation
	c.JSON(200, gin.H{"status": "OK"})
}

