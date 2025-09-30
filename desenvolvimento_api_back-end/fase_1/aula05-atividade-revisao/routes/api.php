<?php

use App\Http\Controllers\AlunoController;
use App\Http\Controllers\CursoController;
use App\Http\Controllers\MatriculaController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::get('/cursos', [CursoController::class, 'index']);
Route::post('/curso', [CursoController::class, 'store']);
Route::get('/curso/{curso}', [CursoController::class, 'show']);
Route::put('/curso/{curso}', [CursoController::class, 'update']);
Route::delete('/curso/{curso}', [CursoController::class, 'destroy']);

Route::get('/alunos', [AlunoController::class, 'index']);
Route::post('/aluno', [AlunoController::class, 'store']);
Route::get('/aluno/{aluno}', [AlunoController::class, 'show']);
Route::put('/aluno/{aluno}', [AlunoController::class, 'update']);
Route::delete('/aluno/{aluno}', [AlunoController::class, 'destroy']);

Route::get('/matriculas', [MatriculaController::class, 'index']);
Route::post('/matricula', [MatriculaController::class, 'store']);
Route::get('/matricula/{matricula}', [MatriculaController::class, 'show']);
Route::put('/matricula/{matricula}', [MatriculaController::class, 'update']);
Route::delete('/matricula/{matricula}', [MatriculaController::class, 'destroy']);