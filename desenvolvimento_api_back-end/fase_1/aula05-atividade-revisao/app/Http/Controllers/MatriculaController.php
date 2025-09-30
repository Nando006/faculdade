<?php

namespace App\Http\Controllers;

use App\Models\Matricula;
use Illuminate\Http\Request;

class MatriculaController extends Controller
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
        return $this->respostaPadrao(message: 'Listando todas as matrículas com sucesso!', data: Matricula::with(['aluno', 'curso'])->get());
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        if(!$request->has('aluno_id') || !$request->has('curso_id')) {
            return [
                'status' => 400,
                'message' => 'Campos obrigatórios vazio',
                'data' => null
            ];
        }

        $data = Matricula::create($request->all());

        return $this->respostaPadrao(message: 'Matricula criada com sucesso', data: $data);
    }

    /**
     * Display the specified resource.
     */
    public function show(Matricula $matricula)
    {
        return $this->respostaPadrao(message: 'Matricula encontrada', data: $matricula->load(['aluno', 'curso']));
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Matricula $matricula)
    {
        if(!$request->has('aluno_id') || !$request->has('curso_id')) {
            return [
                'status' => 400,
                'message' => 'Campos obrigatórios vazio',
                'data' => null
            ];
        }

        $data =$matricula->update($request->all());

        return $this->respostaPadrao(message: 'Matricula atualizada', data: $matricula->load(['aluno', 'curso']));
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Matricula $matricula)
    {
        $matricula->delete();

        return $this->respostaPadrao(message: 'Matricula deletada');
    }
}
