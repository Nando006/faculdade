<?php

namespace App\Http\Controllers;

use App\Models\Aluno;
use Illuminate\Http\Request;

class AlunoController extends Controller
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
        return $this->respostaPadrao(
            message: 'Alunos listado com sucesso',
            data: Aluno::with('matriculas.aluno')->get()
        );
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        if(!$request->has('nome') || !$request->has('email')) {
            return [
                'status' => 400,
                'message' => 'Nome e e-mail são obrigatórios',
                'data' => null
            ];
        }

        $data = Aluno::create($request->all());

        return $this->respostaPadrao(message: 'Aluno criado com sucesso', data: $data);
    }

    /**
     * Display the specified resource.
     */
    public function show(Aluno $aluno)
    {
        return $this->respostaPadrao(message: 'Aluno encontrado!', data: $aluno->load('matriculas.aluno'));
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Aluno $aluno)
    {
        if(!$request->has('nome') || !$request->has('email')) {
            return [
                'status' => 400,
                'message' => 'Nome e e-mail são obrigatórios',
                'data' => null
            ];
        }

        $data = $aluno->update($request->all());

        return $this->respostaPadrao(message: 'Aluno criado com sucesso', data: $data);
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Aluno $aluno)
    {
        $aluno->delete();

        return $this->respostaPadrao(message: 'Aluno deletado com sucesso');
    }
}
