// https://graphology.github.io/standard-library/dag.html
import {DirectedGraph} from 'graphology';
import {topologicalSort} from 'graphology-dag/topological-sort.js';


const graph = new DirectedGraph();
graph.mergeEdge(0, 1);
graph.mergeEdge(1, 2);
graph.mergeEdge(2, 3);

//console.log(graph.isAcyclic()); // true

console.log(topologicalSort(graph)); // [0, 1, 2, 3]

const dag2 = new DirectedGraph();
dag2.mergeEdge(0, 1);
dag2.mergeEdge(0, 2);
dag2.mergeEdge(1, 3);
dag2.mergeEdge(2, 3);
dag2.mergeEdge(3, 4);