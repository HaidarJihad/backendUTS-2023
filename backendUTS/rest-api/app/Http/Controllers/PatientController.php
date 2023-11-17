<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Patient;

class PatientController extends Controller
{
    //
    public function index()
    {
        $patients = Patient::all();
        if ($patients->isEmpty()) {
            return response()->json(204);
        } else {
            $data = [
                'message' => 'The request succeeded',
                'data' => $patients,
            ];

            return response()->json($data, 200);
        }
    }

    public function store(Request $request)
    {
        $request->validate([
            'name' => 'required',
            'phone' => 'required',
            'address' => 'required',
            'status' => 'required',
            'in_date_at' => 'required',
            'out_date_at' => 'required'
        ]);

        $input = [
            'name' => $request->name,
            'phone' => $request->phone,
            'address' => $request->address,
            'status' => $request->status,
            'in_date_at' => $request->in_date_at,
            'out_date_at' => $request->out_date_at,
        ];

        $patients = Patient::create($input);

        $data = [
            'message' => 'Resource created',
            'data' => $patients,
        ];

        return response()->json($data, 201);
    }

    public function update(Request $request, $id)
    {
        $patients = Patient::find($id);

        if ($patients) {
            $input = [
                'name' => $request->name ?? $patients->name,
                'phone' => $request->phone ?? $patients->phone,
                'address' => $request->address ?? $patients->address,
                'status' => $request->status ?? $patients->status,
                'name' => $request->name ?? $patients->name,
                'in_date_at' => $request->in_date_at ?? $patients->in_date_at,
                'out_date_at' => $request->out_date_at ?? $patients->out_date_at,
            ];

            $patients->update($input);

            $data = [
                'message' => 'The request succeeded',
                'data' => $patients,
            ];

            return response()->json($data, 200);
        } else {
            $data = [
                'message' => 'Resource not found'
            ];
            return response()->json($data, 404);
        }
    }

    public function show($id)
    {
        $patients = Patient::find($id);

        if ($patients) {
            $data =[
                'message' => 'Unauthenticat',
                'data' => $patients,
            ];

            return response()->json($data, 401);
        } else {
            $data = [
                'message' => 'Pasient not found',
            ];

            return response()->json($data, 404);
        }
    }
}
