# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY

variable "username" {
  description = "Master username of the DB"
  default = "arcane"
}

variable "password" {
  description = "Master password of the DB"
}

variable "database_name" {
  description = "Name of the database to be created"
  default = "arcane"
}

variable "name" {
  description = "Name of the database"
  default     = "arcane-1"
}

variable "engine_name" {
  description = "Name of the database engine"
  default     = "mysql"
}

variable "family" {
  description = "Family of the database"
  default     = "mysql5.7"
}

variable "port" {
  description = "Port which the database should run on"
  default     = 3306
}

variable "major_engine_version" {
  description = "MAJOR.MINOR version of the DB engine"
  default     = "5.7"
}

variable "engine_version" {
  default     = "5.7.21"
  description = "Version of the database to be launched"
}

variable "allocated_storage" {
  default     = 5
  description = "Disk space to be allocated to the DB instance"
}

variable "license_model" {
  default     = "general-public-license"
  description = "License model of the DB instance"
}