/*
Position of element in flags_for_js at moment not used
Used try and catch
0: select_color_node
1: drag_node: possibility to drag the node
2: remove_edge: delete a selected edge
3: remove_node: delete a selected node
4: add_node: add a node
5: add_edge: add an edge
6: choice: possibility to chioice between yes or no 
7: edit_label: label on edge or node are editable (TODO)
*/
/*
For camera e drag node use no_editable
0: camera
1: drag node
*/
var g = $graph_data;
//var flags_for_js = $data;
var not_editable = $data;

var default_color_node = "#1e6add";
var default_color_edge = "#1e6add";
var color_first_set = "#FF5722";
var color_second_set = "#FFD600";
var size_edge = 3;
var size_node = 5;

s = new sigma({
    graph: g,
    renderer: {
        container: document.getElementById('$container'),
        type: 'canvas'
    },
    settings: {
        minNodeSize: 3,
        maxNodeSize: 10,
        minEdgeSize: 2,
        maxEdgeSize: 4,
        zoomMin: 0.01,
        zoomMax: 5,
        zoomingRatio: 0.9,
        enableEdgeHovering: true,
        doubleClickEnabled: false,
        defaultNodeColor: default_color_node,
        edgeHoverColor: 'edge',
        defaultEdgeHoverColor: "#4CAF50",
        borderSize: 4,
        doubleClickEnabled: false,
        arrowSizeRatio: 5,
        sideMargin: 0.1,
        autoRescale: ['nodePosition', 'nodeSize', 'edgeSize'],
        rescaleIgnoreSize: true,
        enableHovering: false,
        autoResize: false
    }
});

if(not_editable[0] == "true"){
    s.settings('enableCamera', false)
}

if (not_editable[1] == "true") {
    sigma.plugins.dragNodes(s, s.renderers[0]);
}
var kernel = IPython.notebook.kernel;
var nodes_added = 1
var edges_added = 1
var remove_node = false
var remove_edge = false
var source = false
var target = false
var set_one = false // red 
var set_two = false // yellow
var unselect_set = false // black


s.bind('clickNode', function(e) {
    var node = e.data.node;
    var nodeId = node.id

    if (target) {
        var new_edge_id = "e_a_" + source_id + "" + nodeId
        s.graph.addEdge({ id: new_edge_id, source: source_id, target: nodeId, type: "arrow", color: default_color_edge, size: size_edge, hover_color: "#4CAF50" });
        command_4 = "added_edges.append(('" + source_id + "','" + nodeId + "'))"
        kernel.execute(command_4);
        source_id = null
        target_id = null
        target = false
    } else if (source) {
        source_id = nodeId
        source = false
        target = true
    } else if (remove_node) { //rimuovi arco in python?
        command_0 = "if '" + nodeId + "' in first_set: first_set.remove('" + nodeId + "')"
        command_1 = "if '" + nodeId + "' in second_set: second_set.remove('" + nodeId + "')"
        command_2 = "removed_nodes.append('" + nodeId + "')"
        command_3 = "remove_edges_of_node('" + nodeId + "')"
        console.log(command_3)
        kernel.execute(command_0);
        kernel.execute(command_1);
        kernel.execute(command_2);
        kernel.execute(command_3)
        s.graph.dropNode(nodeId)
        s.refresh()
        remove_node = false
        return
    } else if (set_one) {   
        old_color = node.color
        node.color = current_color;
        s.refresh()
        if (old_color == color_second_set){
            command_r = "second_set.remove('"+nodeId+"')"
            kernel.execute(command_r);
        }
        command = "first_set.append('"+nodeId+"')"
        kernel.execute(command);
    } else if (set_two) {       
        old_color = node.color
        node.color = current_color;
        s.refresh()
        if (old_color == color_first_set){
            command_r = "first_set.remove('"+nodeId+"')"
            kernel.execute(command_r);
        }

        command = "second_set.append('"+nodeId+"')"
        kernel.execute(command);
    } else if (unselect_set) {       
        old_color = node.color
        node.color = current_color;
        s.refresh()
        if (old_color == color_first_set){
            command_r = "first_set.remove('"+nodeId+"')"
            kernel.execute(command_r);
        }
        if (old_color == color_second_set){
            command_r = "second_set.remove('"+nodeId+"')"
            kernel.execute(command_r);
        }
    }
    s.refresh()
});


s.bind('clickEdge', function(event) {
    var edge = event.data.edge;
    var edgeId = edge.id
    if (remove_edge) {
        s.graph.dropEdge(edgeId)
        s.refresh()
        command_2 = "removed_edges.append(('"+edge.source+"','"+edge.target+"'))"
        kernel.execute(command_2)
        to_remove_e = false        
        return
    } else if (set_one) {
        if (edge.color == color_second_set) {
            command_r = "second_set_edge.remove(('" + edge.source + "','" + edge.target + "'))"
            kernel.execute(command_r);
        }
        edge.color = current_color;
        command = "first_set_edge.append(('" + edge.source + "','" + edge.target + "'))"
        kernel.execute(command);
    } else if (set_two) {
        if (edge.color == color_first_set) {
            command_r = "first_set_edge.remove(('" + edge.source + "','" + edge.target + "'))"
            kernel.execute(command_r);
        }
        edge.color = current_color;
        command = "second_set_edge.append(('" + edge.source + "','" + edge.target + "'))"
        kernel.execute(command);
    } else if (unselect_set) {
        if (edge.color == color_first_set) {
            command_r = "first_set_edge.remove(('" + edge.source + "','" + edge.target + "'))"
            kernel.execute(command_r);
        }
        if (edge.color == color_second_set) {
            command_r = "second_set_edge.remove(('" + edge.source + "','" + edge.target + "'))"
            kernel.execute(command_r);
        }
        edge.color = default_color_edge;
    }
    s.refresh()
});

//if (flags_for_js[5] == "true") {
try{
    //add edge
    document.getElementById("btn_add_e").addEventListener("click", function() {
        set_one = false
        set_two = false
        unselect_set = false
        source = true
        target = false

    });
}catch(e){};
//}
//if (flags_for_js[6] === "true") {
try{
    //yes choice
    document.getElementById("yes").addEventListener("click", yes);

    function yes() {
        set_one = false
        set_two = false
        unselect_set = false
        var scelta = document.getElementById("yes").value
        command = "choice='" + scelta + "'"
        kernel.execute(command)
    };

    //no choice
    document.getElementById("no").addEventListener("click", no);

    function no() {
        set_one = false
        set_two = false
        unselect_set = false
        var scelta = document.getElementById("no").value
        command = "choice='" + scelta + "'"
        kernel.execute(command)
    };
}catch(e){};
//}
//if (flags_for_js[4] == "true") {
    //add node
try{
    document.getElementById("btn_add").addEventListener("click", function() {
        set_one = false
        set_two = false
        unselect_set = false
        newNodeId = 'added' + nodes_added
        s.graph.addNode({ id: newNodeId, label: 'add' + nodes_added, x: 1, y: 1, size: size_node });
        command_1 = "added_nodes.append('" + newNodeId + "')"
        kernel.execute(command_1);
        nodes_added = nodes_added + 1;
        s.refresh();
    });
}catch(e){};
//}
//if (flags_for_js[0] == "true") {
try {
    //selezione colori
    document.getElementById("btn_set_one").style.backgroundColor= color_first_set
    document.getElementById("btn_set_one").addEventListener("click", function() {
        set_two = false
        unselect_set = false
        set_one = true
        remove_node = false;
        remove_edge = false;
        current_color = color_first_set

        
    });
    var for_bg = document.getElementById("btn_set_two");
    for_bg.style.backgroundColor= color_second_set;
    for_bg.style.color="black";
    document.getElementById("btn_set_two").addEventListener("click", function() {
        set_one = false
        set_two = true
        unselect_set = false
        remove_edge = false;
        remove_node = false;
        current_color = color_second_set
    });
    
    var for_bg = document.getElementById("btn_unselect_set");
    for_bg.style.backgroundColor= default_color_node;
    document.getElementById("btn_unselect_set").addEventListener("click", function() {
        set_one = false
        set_two = false
        unselect_set = true
        remove_node = false;
        remove_edge = false;
        current_color = default_color_node;
    });
}catch(e){};
//}

//if (flags_for_js[3] == "true") {
try{
    //remove node
    document.getElementById("btn_remove").addEventListener("click", remove);

    function remove() {
        set_one = false
        set_two = false
        unselect_set = false
        remove_node = true;
        remove_edge = false;
    }
}catch(e){};
//}


//if (flags_for_js[2] == "true") {
    //remove edge
try{
    document.getElementById("btn_remove_e").addEventListener("click", remove_e);

    function remove_e() {
        set_one = false
        set_two = false
        unselect_set = false
        remove_edge = true;
        remove_node = false;
    }
}catch(e){};
//}