/**
 *
 * Please note:
 * This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * Do not edit this file manually.
 *
 */

@file:Suppress(
    "ArrayInDataClass",
    "EnumEntryName",
    "RemoveRedundantQualifierName",
    "UnusedImport"
)

package org.openapitools.client.models


import com.fasterxml.jackson.annotation.JsonEnumDefaultValue
import com.fasterxml.jackson.annotation.JsonProperty

/**
 * An order for a pets from the pet store
 *
 * @param id 
 * @param petId 
 * @param quantity 
 * @param shipDate 
 * @param status Order Status
 * @param complete 
 */


data class Order (

    @field:JsonProperty("id")
    val id: kotlin.Long? = null,

    @field:JsonProperty("petId")
    val petId: kotlin.Long? = null,

    @field:JsonProperty("quantity")
    val quantity: kotlin.Int? = null,

    @field:JsonProperty("shipDate")
    val shipDate: java.time.OffsetDateTime? = null,

    /* Order Status */
    @field:JsonProperty("status")
    val status: Order.Status? = null,

    @field:JsonProperty("complete")
    val complete: kotlin.Boolean? = false

) {

    /**
     * Order Status
     *
     * Values: PLACED,APPROVED,DELIVERED,UNKNOWN_DEFAULT_OPEN_API
     */
    enum class Status(val value: kotlin.String) {
        @JsonProperty(value = "placed") PLACED("placed"),
        @JsonProperty(value = "approved") APPROVED("approved"),
        @JsonProperty(value = "delivered") DELIVERED("delivered"),
        @JsonProperty(value = "unknown_default_open_api") @JsonEnumDefaultValue UNKNOWN_DEFAULT_OPEN_API("unknown_default_open_api");
    }
}

