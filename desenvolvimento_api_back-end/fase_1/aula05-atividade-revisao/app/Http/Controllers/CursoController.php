<?php

namespace App\Http\Controllers;

use App\Models\Curso;
use Illuminate\Http\Request;

class CursoController extends Controller
{
    private function respostaPadrao($message = 'Resposta obitida com sucesso', $data = null) {
        return [
            'status' => 200,
            'message' => $message,
            'data' => $data
        ];
    }

    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return $this->respostaPadrao(data: Curso::with('matriculas.aluno')->get());
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        if(!$request->has('titulo')) {
            return [
                'status' => 400,
                'message' => 'Campos obrigatórios não informados',
                'data' => null
            ];
        }

        return $this->respostaPadrao(message: 'Curso criado com sucesso!' ,data: Curso::create($request->all()));
    }

    /**
     * Display the specified resource.
     */
    public function show(Curso $curso)
    {
        return $this->respostaPadrao(message: 'Curso encontrado com sucesso!' ,data: $curso->load('matriculas.aluno'));
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Curso $curso)
    {
        if(!$request->has('titulo')) {
            return [
                'status' => 400,
                'message' => 'Campos obrigatórios não informados',
                'data' => null
            ];
        }

        return $this->respostaPadrao(message: 'Curso atualizado com sucesso!' ,data: $curso->update($request->all()));
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Curso $curso)
    {
        $curso->delete();

        return $this->respostaPadrao(message: 'Curso deletado com sucesso!');
    }
}
