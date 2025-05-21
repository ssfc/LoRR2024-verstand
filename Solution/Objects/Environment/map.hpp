#pragma once

#include <SharedEnv.h>

#include <cstdint>
#include <vector>

// Contains information about map:
// rows, cols, is_free
// 0 = NONE
class Map {
    uint32_t rows = 0;
    uint32_t cols = 0;

    uint32_t cnt_free = 0;

    std::vector<bool> map;

public:
    Map() = default;

    explicit Map(const SharedEnvironment &env);

    [[nodiscard]] uint32_t get_rows() const;

    [[nodiscard]] uint32_t get_cols() const;

    [[nodiscard]] uint32_t get_size() const;

    [[nodiscard]] uint32_t get_count_free() const;

    [[nodiscard]] bool is_free(uint32_t pos) const;
};

Map &get_map();
