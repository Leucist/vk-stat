## VK-status changing bot

[![Version](https://img.shields.io/badge/version-1.2-green.svg)](https://github.com/Leucist/vk-stat)

> Author: [leucist](https://github.com/Leucist)

This is a Python project, which uses VK API and 'time' library in order to change status at 00:00 (GMT+3) daily in "v_*age*.*days-after-birthday*"-format (example: "v_17.217")

! Status has to be already properly formatted\
! 'logs.json' file is required and must contain such data:
```json
{
    "login": "Your VK login",
    "password": "Your VK password"
}
```
