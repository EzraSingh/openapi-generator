<?php
/**
 * Order
 *
 * PHP version 8.1.1
 *
 * @category Class
 * @package  OpenAPI\Server\Model
 * @author   OpenAPI Generator team
 * @link     https://github.com/openapitools/openapi-generator
 */

/**
 * OpenAPI Petstore
 *
 * This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 *
 */

/**
 * NOTE: This class is auto generated by the openapi generator program.
 * https://github.com/openapitools/openapi-generator
 * Do not edit the class manually.
 */

namespace OpenAPI\Server\Model;

use Symfony\Component\Validator\Constraints as Assert;
use JMS\Serializer\Annotation\Type;
use JMS\Serializer\Annotation\Accessor;
use JMS\Serializer\Annotation\SerializedName;

/**
 * Class representing the Order model.
 *
 * An order for a pets from the pet store
 *
 * @package OpenAPI\Server\Model
 * @author  OpenAPI Generator team
 */

class Order 
{
        /**
     * @var int|null
     * @SerializedName("id")
     * @Assert\Type("int")
     * @Type("int")
     */
    protected ?int $id = null;

    /**
     * @var int|null
     * @SerializedName("petId")
     * @Assert\Type("int")
     * @Type("int")
     */
    protected ?int $petId = null;

    /**
     * @var int|null
     * @SerializedName("quantity")
     * @Assert\Type("int")
     * @Type("int")
     */
    protected ?int $quantity = null;

    /**
     * @var \DateTime|null
     * @SerializedName("shipDate")
     * @Assert\Type("\DateTime"))
     * @Type("DateTime")
     */
    protected ?\DateTime $shipDate = null;

    /**
     * Order Status
     *
     * @var string|null
     * @SerializedName("status")
     * @Assert\Choice({ "placed", "approved", "delivered" })
     * @Assert\Type("string")
     * @Type("string")
     */
    protected ?string $status = null;

    /**
     * @var bool|null
     * @SerializedName("complete")
     * @Assert\Type("bool")
     * @Type("bool")
     */
    protected ?bool $complete = false;

    /**
     * Constructor
     * @param array|null $data Associated array of property values initializing the model
     */
    public function __construct(array $data = null)
    {
        if (is_array($data)) {
            $this->id = array_key_exists('id', $data) ? $data['id'] : $this->id;
            $this->petId = array_key_exists('petId', $data) ? $data['petId'] : $this->petId;
            $this->quantity = array_key_exists('quantity', $data) ? $data['quantity'] : $this->quantity;
            $this->shipDate = array_key_exists('shipDate', $data) ? $data['shipDate'] : $this->shipDate;
            $this->status = array_key_exists('status', $data) ? $data['status'] : $this->status;
            $this->complete = array_key_exists('complete', $data) ? $data['complete'] : $this->complete;
        }
    }

    /**
     * Gets id.
     *
     * @return int|null
     */
    public function getId(): ?int
    {
        return $this->id;
    }



    /**
     * Sets id.
     *
     * @param int|null $id
     *
     * @return $this
     */
    public function setId(?int $id = null): self
    {
        $this->id = $id;

        return $this;
    }

    /**
     * Gets petId.
     *
     * @return int|null
     */
    public function getPetId(): ?int
    {
        return $this->petId;
    }



    /**
     * Sets petId.
     *
     * @param int|null $petId
     *
     * @return $this
     */
    public function setPetId(?int $petId = null): self
    {
        $this->petId = $petId;

        return $this;
    }

    /**
     * Gets quantity.
     *
     * @return int|null
     */
    public function getQuantity(): ?int
    {
        return $this->quantity;
    }



    /**
     * Sets quantity.
     *
     * @param int|null $quantity
     *
     * @return $this
     */
    public function setQuantity(?int $quantity = null): self
    {
        $this->quantity = $quantity;

        return $this;
    }

    /**
     * Gets shipDate.
     *
     * @return \DateTime|null
     */
    public function getShipDate(): ?\DateTime
    {
        return $this->shipDate;
    }



    /**
     * Sets shipDate.
     *
     * @param \DateTime|null $shipDate
     *
     * @return $this
     */
    public function setShipDate(?\DateTime $shipDate = null): self
    {
        $this->shipDate = $shipDate;

        return $this;
    }

    /**
     * Gets status.
     *
     * @return string|null
     */
    public function getStatus(): ?string
    {
        return $this->status;
    }



    /**
     * Sets status.
     *
     * @param string|null $status  Order Status
     *
     * @return $this
     */
    public function setStatus(?string $status = null): self
    {
        $this->status = $status;

        return $this;
    }

    /**
     * Gets complete.
     *
     * @return bool|null
     */
    public function isComplete(): ?bool
    {
        return $this->complete;
    }



    /**
     * Sets complete.
     *
     * @param bool|null $complete
     *
     * @return $this
     */
    public function setComplete(?bool $complete = null): self
    {
        $this->complete = $complete;

        return $this;
    }
}


