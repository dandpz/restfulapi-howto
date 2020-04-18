/*
 * TO-DO list
 *
 * This is an example server for TO-DO list.  This is part of the collection of articles dedicated to the development of RESTful API. To know more visit the [repository](https://github.com/dandpz/restfulapi-howto) containing the code for these examples and more.
 *
 * API version: 1.0.0
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

type PaginatedResponseData struct {
	// Total amount of resource
	Total int32 `json:"total,omitempty"`
	// Count of the resources in the current response
	Count int32 `json:"count,omitempty"`
	// Page number
	Page int32 `json:"page,omitempty"`
	// Number of resource per page
	Size int32 `json:"size,omitempty"`
	// Resources
	Resources []interface{} `json:"resources,omitempty"`
}
