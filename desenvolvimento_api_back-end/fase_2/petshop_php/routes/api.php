<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::prefix('/cliente')->group(function () {
    Route::post('/cadastrar', [ClienteController::class, 'salvar']);
    
    Route::get('/listar', [ClienteController::class, 'listar']);

    Route::put('/atualizar/{id}', [ClienteController::class, 'atualizar']);

    Route::delete('/deletar/{id}', [ClienteController::class, 'deletar']);
});
