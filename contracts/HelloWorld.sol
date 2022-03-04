// SPDX-license-Identifier: MIT

pragma solidity ^0.6.6;

contract HelloWorld {
    string message;

    constructor(string memory _message) public {
        message = _message;
    }

    function GetMessage() public view returns (string memory) {
        return message;
    }

    function UpdateMessage(string memory _NewMessage) public {
        message = _NewMessage;
    }
}
