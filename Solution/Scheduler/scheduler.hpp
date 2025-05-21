#pragma once

#include <Scheduler/scheduler_solver.hpp>

#include <SharedEnv.h>
#include <Tasks.h>

// MyScheduler在scheduler.hpp里面定义
struct MyScheduler {

    SharedEnvironment *env = nullptr;

    SchedulerSolver solver;

    MyScheduler() = default;

    explicit MyScheduler(SharedEnvironment *env);

    void plan(TimePoint end_time, std::vector<int> &proposed_schedule);

    void solver_schedule(TimePoint end_time, std::vector<int> &proposed_schedule);

    std::vector<int> artem_schedule(int time_limit, std::vector<int> &proposed_schedule);
};
