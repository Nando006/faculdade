<?php

namespace App\Http\Controllers;

use App\Models\Distribuidora;
use Illuminate\Http\Request;

class DistribuidoraController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $data = Distribuidora::all();

        return [
            'status' => 200,
            'message' => 'Distribuidoras listadas com sucesso!',
            'data' => $data
        ];
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $data = Distribuidora::create($request->all());

        return [
            'status' => 200,
            'message' => 'Distribuidora criada com sucesso!',
            'data' => $data
        ];
    }

    /**
     * Display the specified resource.
     */
    public function show(Distribuidora $distribuidora)
    {
        return [
            'status' => 200,
            'message' => 'Distribuidora encontrada',
            'data' => $distribuidora
        ];
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Distribuidora $distribuidora)
    {
        return [
            'status' => 200,
            'message' => 'Distribuidora atualizado com sucesso!',
            'data' => $distribuidora->update($request->all()),
        ];
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Distribuidora $distribuidora)
    {
        return [
            'status' => 200,
            'message' => 'Distribuidora deletado com sucesso!',
            'data' => $distribuidora->delete(),
        ];
    }
}
