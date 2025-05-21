#!/bin/bash

# RANDOM-01
for i in {1..10}; do
    ./lifelong --inputFile ./2024main-instance/Main\ Round\ Evaluation\ Instances/random.domain/RANDOM-01.json -o test_main_round.json -s 600 -p 1800000;
done

# RANDOM-02
for i in {1..10}; do
    ./lifelong --inputFile ./2024main-instance/Main\ Round\ Evaluation\ Instances/random.domain/RANDOM-02.json -o test_main_round.json -s 600 -p 1800000;
done

# RANDOM-03
for i in {1..10}; do
    ./lifelong --inputFile ./2024main-instance/Main\ Round\ Evaluation\ Instances/random.domain/RANDOM-03.json -o test_main_round.json -s 800 -p 1800000;
done

# RANDOM-04
for i in {1..10}; do
    ./lifelong --inputFile ./2024main-instance/Main\ Round\ Evaluation\ Instances/random.domain/RANDOM-04.json -o test_main_round.json -s 1000 -p 1800000;
done

# RANDOM-05
for i in {1..10}; do
    ./lifelong --inputFile ./2024main-instance/Main\ Round\ Evaluation\ Instances/random.domain/RANDOM-05.json -o test_main_round.json -s 2000 -p 1800000;
done

# CITY-01
for i in {1..10}; do
    ./lifelong --inputFile ./2024main-instance/Main\ Round\ Evaluation\ Instances/city.domain/CITY-01.json -o test_main_round.json -s 3000 -p 1800000;
done

# CITY-02
for i in {1..10}; do
    ./lifelong --inputFile ./2024main-instance/Main\ Round\ Evaluation\ Instances/city.domain/CITY-02.json -o test_main_round.json -s 3000 -p 1800000;
done

# GAME
for i in {1..10}; do
    ./lifelong --inputFile ./2024main-instance/Main\ Round\ Evaluation\ Instances/game.domain/GAME.json -o test_main_round.json -s 5000 -p 1800000;
done

# SORTATION
for i in {1..10}; do
    ./lifelong --inputFile ./2024main-instance/Main\ Round\ Evaluation\ Instances/warehouse.domain/SORTATION.json -o test_main_round.json -s 5000 -p 1800000;
done

# WAREHOUSE
for i in {1..10}; do
    ./lifelong --inputFile ./2024main-instance/Main\ Round\ Evaluation\ Instances/warehouse.domain/WAREHOUSE.json -o test_main_round.json -s 5000 -p 1800000;
done
