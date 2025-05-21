#pragma once

#include <Objects/Environment/graph.hpp>

class HeuristicMatrix {
    // matrix[target (map pos)][source (graph node)] = dist[source -> target]
    std::vector<std::vector<uint16_t>> matrix;

    // 它利用了类似于 Dijkstra 算法的逻辑从指定源点 source 开始计算图中所有节点的最短路径并存储结果。
    void build(uint32_t source, const Graph &graph);

public:
    HeuristicMatrix() = default;

    explicit HeuristicMatrix(const Graph &graph);

    // source is graph node
    // target is map pos
    // if dest is NONE(zero), then returns INVALID_DIST
    [[nodiscard]] uint32_t get(uint32_t source, uint32_t target) const;
};

HeuristicMatrix &get_hm();
