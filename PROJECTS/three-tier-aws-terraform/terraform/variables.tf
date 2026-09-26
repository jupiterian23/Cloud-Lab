variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "three-tier-aws"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "db_username" {
  description = "Database administrator username"
  type        = string
  default     = "appadmin"
}

variable "db_password" {
  description = "Database administrator password"
  type        = string
  sensitive   = true
}
