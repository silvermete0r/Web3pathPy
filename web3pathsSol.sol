pragma solidity ^0.8.0;

contract PathFinder {
    
    mapping(address => targetAddress) public parent;

    function setParent(address _node, address _parent) public {
        require(msg.sender == address(this), "Allowed only for the owner!");
        parent[_node] = _parent;
    }

    function findPaths(address _start, address _end) public view returns (address[][] memory) {
        targetAddress[][] memory paths = [];
        paths.push([_start]);
        if (_start == _end) {
            return paths;
        }

        for (address node in parent) {
            if (parent[node] == _start) {
                targetAddress[][] memory subpaths = findPaths(node, _end);
                for (uint i = 0; i < subpaths.length; i++) {
                    paths.push([_start] + subpaths[i]);
                }
            }
        }
        return paths;
    }
}