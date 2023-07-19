#!/usr/bin/python3
#coding=utf8

import requests

class WbApi:
    ADS_TYPES = [
            "test",
            "balance",
            "budget",
            "count",
            "adverts",
            "advert",
            "start",
            "pause",
            "stop",
            "cpm",
            "cpmch",
            "allcpm",
            "active",
            ""
    ]

    def __init__(self, token_base: str, token_adv: str, token_stat: str):
        
        self.token_base = token_base
        self.token_adv = token_adv
        self.token_stat = token_stat

    
    # Checking validity
    def _check_token_base(self) -> bool:
        if not self.token_base:
            return False
        if not self._get_base("test"):
            return False
        return True
    
    def _check_token_adv(self) -> bool:
        if not self.token_adv:
            return False
        if not self._get_adv("test"):
            return False
        return True
    
    def _check_token_stat(self) -> bool:
        if not self.token_stat:
            return False
        if not self._get_stat("test"):
            return False
        return True
    

    # Public 
    # Checking validity
    def check_all(self) -> tuple:
        status = (
                self._check_token_base(),
                self._check_token_adv(),
                self._check_token_stat()
        )
        return status

    def check_token_base(self) -> bool:
        return self._check_token_base()
    
    def check_token_adv(self) -> bool:
        return self._check_token_adv()
    
    def check_token_stat(self) -> bool:
        return self._check_token_stat()


    # Ads
    def _get_adv(gettype: str) -> dict:
        response = {}
        
        if gettype not in self.ADS_TYPES:
            return response

        


