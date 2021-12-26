import mysql.connector
import sys


def create(db):
    cursor = db.cursor()
    try:
        cursor.execute("CREATE DATABASE mds;")
        cursor.execute("CREATE TABLE `mds`.`customers` ("
                       "`pk` INT UNSIGNED NOT NULL AUTO_INCREMENT, "
                       "`group_code` VARCHAR(45) NULL, "
                       "`group_desc` TEXT NULL, "
                       "`code` VARCHAR(45) NULL,"
                       "`code_desc` TEXT NULL,"
                       " PRIMARY KEY (`pk`)); ")
    except:
        cursor.execute("CREATE TABLE `mds`.`customers` ("
                       "`pk` INT UNSIGNED NOT NULL AUTO_INCREMENT, "
                       "`group_code` VARCHAR(45) NULL, "
                       "`group_desc` TEXT NULL, "
                       "`code` VARCHAR(45) NULL,"
                       "`code_desc` TEXT NULL,"
                       " PRIMARY KEY (`pk`)); ")
    return True

