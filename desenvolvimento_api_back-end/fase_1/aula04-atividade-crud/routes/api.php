<?php

use App\Http\Controllers\CategoriaController;
use App\Http\Controllers\DistribuidoraController;
use App\Http\Controllers\ProdutoController;
use App\Http\Controllers\UserController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::apiResource('/users', UserController::class);
Route::apiResource('/distribuidora', DistribuidoraController::class);
Route::apiResource('/categoria', CategoriaController::class);
Route::apiResource('/produto', ProdutoController::class);
