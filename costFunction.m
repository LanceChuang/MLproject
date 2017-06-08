
% this function can evaluate 2 functions for given input values theta


function [ jVal, gradient ] = costFunction(theta)

jVal = (theta(1) - 5) ^ 2 + (theta(2) - 5) ^ 2;

gradient = zeros(2,1) % 2 row 1 col
gradient(1) = 2 * (theta(1) - 5);
gradient(2) = 2 * (theta(2) - 5); 
end

